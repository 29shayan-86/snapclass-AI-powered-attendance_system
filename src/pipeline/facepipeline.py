import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC

import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():

    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):

    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:

        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(
            np.array(face_descriptor)
        )

    return encodings


def get_students_signature(student_db):

    signature = []

    for student in student_db:

        student_id = student.get("student_id")
        embedding = student.get("face_embedding")

        if embedding:

            signature.append(
                (
                    student_id,
                    tuple(embedding)
                )
            )

    return tuple(signature)


@st.cache_resource
def get_trained_model(student_signature):

    X = []
    y = []

    for student_id, embedding in student_signature:

        X.append(
            np.array(embedding)
        )

        y.append(student_id)

    if len(X) == 0:
        return None

    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    try:

        clf.fit(X, y)

    except ValueError:

        return None

    return {
        "clf": clf,
        "X": X,
        "y": y
    }


def train_classifier():

    # Clear cached SVM models
    get_trained_model.clear()

    # Load current students
    student_db = get_all_students()

    # Create signature from current database
    student_signature = get_students_signature(
        student_db
    )

    # Train using current database
    model_data = get_trained_model(
        student_signature
    )

    return bool(model_data)


def predict_attendance(class_image_np):

    encodings = get_face_embeddings(
        class_image_np
    )

    detected_student = {}

    # Always get the CURRENT database
    student_db = get_all_students()

    # Create signature based on current students
    student_signature = get_students_signature(
        student_db
    )

    # Get model for current database
    model_data = get_trained_model(
        student_signature
    )

    if not model_data:

        return (
            detected_student,
            [],
            len(encodings)
        )

    clf = model_data["clf"]

    X_train = model_data["X"]

    y_train = model_data["y"]

    all_students = sorted(
        list(set(y_train))
    )

    for encoding in encodings:

        if len(all_students) >= 2:

            predicted_id = int(
                clf.predict([encoding])[0]
            )

        else:

            predicted_id = int(
                all_students[0]
            )

        student_embedding = X_train[
            y_train.index(predicted_id)
        ]

        best_match_score = np.linalg.norm(
            student_embedding - encoding
        )

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:

            detected_student[predicted_id] = True

    return (
        detected_student,
        all_students,
        len(encodings)
    )