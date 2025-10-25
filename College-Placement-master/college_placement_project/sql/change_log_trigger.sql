-- Create a sequence for generating auto-increment values
CREATE SEQUENCE student_roll_number_seq
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1;
--    MAXVALUE 9999;

-- Create a function to generate the custom roll_number
CREATE OR REPLACE FUNCTION generate_student_roll_number()
    RETURNS TRIGGER AS $$
BEGIN
    NEW.roll_number := 'B2323R' || TO_CHAR(nextval('student_roll_number_seq'), 'FM0000');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to call the function before inserting a new row
CREATE TRIGGER before_insert_student
    BEFORE INSERT ON placement_app_students
    FOR EACH ROW
    EXECUTE FUNCTION generate_student_roll_number();
