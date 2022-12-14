-- UPDATE [assessment_assessment] SET [slug] = (SELECT slug FROM assessment_assessment WHERE id = 3) + 1 WHERE id not in (1, 3 , 4, 51, 52);

-- SELECT * FROM assessment_assessment;