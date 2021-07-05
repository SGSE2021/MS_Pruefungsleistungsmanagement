CREATE TABLE assessment (
    assessment_id INT PRIMARY KEY AUTO_INCREMENT,
    course_course_id INT NOT NULL,
    topic VARCHAR(255) NOT NULL,
    start_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    end_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    state VARCHAR(255) NOT NULL,
    is_rated BOOLEAN NOT NULL,
    max_rating INT NOT NULL,
    rating INT,
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

CREATE TABLE document (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    assessment_assessment_id INT,
    doc_name VARCHAR(255) NOT NULL,
    doc_data MEDIUMBLOB,
    FOREIGN KEY(assessment_assessment_id) REFERENCES assessment(assessment_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO
    document (
        document_id,
        assessment_assessment_id,
        doc_name
    )
VALUES
    (1, 1, 'Test file');

CREATE TABLE question (
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    assessment_assessment_id INT,
    is_multiple_choice BOOLEAN NOT NULL,
    question VARCHAR(255) NOT NULL,
    points INT NOT NULL,
    answer VARCHAR(255),
    FOREIGN KEY(assessment_assessment_id) REFERENCES assessment(assessment_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO
    question (
        assessment_assessment_id,
        is_multiple_choice,
        question,
        points,
        answer
    )
VALUES
    (
        1,
        0,
        'Test Question 1',
        0,
        'Test Answer 1'
    );

CREATE TABLE answer (
    answer_id INT PRIMARY KEY AUTO_INCREMENT,
    question_question_id INT,
    answer_text VARCHAR(255) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    is_checked BOOLEAN NOT NULL,
    FOREIGN KEY(question_question_id) REFERENCES question(question_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO
    answer (
        question_question_id,
        answer_text,
        is_correct,
        is_checked
    )
VALUES
    (
        2,
        'Answer Text 1',
        1,
        0
    );