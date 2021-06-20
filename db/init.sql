CREATE TABLE assessment (
    assessment_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    course_course_id INT(11) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    start_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    end_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    state VARCHAR(255) NOT NULL,
    is_rated BOOLEAN NOT NULL,
    max_rating INT(11) NOT NULL,
    rating INT(11),
    created DATETIME DEFAULT CURRENT_TIMESTAMP(),
    updated DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()
);

INSERT INTO
    assessment (
        course_course_id,
        topic,
        state,
        is_rated,
        max_rating,
        rating
    )
VALUES
    (
        1,
        'Das ist ein Test Thema',
        'erstellt',
        0,
        10,
        8
    );

CREATE TABLE answer (
    answer_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    answer_text VARCHAR(255) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    is_checked BOOLEAN NOT NULL,
);

CREATE TABLE question (
    question_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    answer_answer_id INT(11),
    assessment_assessment_id INT(11),
    FOREIGN KEY(answer_answer_id) REFERENCES answer(answer_id),
    FOREIGN KEY(assessment_assessment_id) REFERENCES assessment(assessment_id),
    is_multiple_choice BOOLEAN NOT NULL,
    question VARCHAR(255) NOT NULL,
    points INT(11) NOT NULL,
    answer VARCHAR(255)
);

CREATE TABLE document (
    document_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    assessment_assessment_id INT(11),
    FOREIGN KEY(assessment_assessment_id) REFERENCES assessment(assessment_id),
    doc_name VARCHAR(255) NOT NULL,
    doc_data MEDIUMBLOB
);

INSERT INTO
    document (
        assessment_assessment_id,
        doc_name
    )
VALUES
    (2, 'test-doc1'),
    (1, 'test-doc2');