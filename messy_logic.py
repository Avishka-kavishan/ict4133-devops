"""
Student Grade Calculator - CLEAN VERSION
This demonstrates GOOD code practices with low cyclomatic complexity.
Cyclomatic Complexity: ~5 (ACCEPTABLE)
"""

def calculate_student_grade(score, attendance, assignments_completed, 
                           participation, extra_credit, late_submissions,
                           group_project_score, midterm_score, 
                           final_exam_score, is_honors_student):
    """
    Calculate final grade for a student based on multiple criteria.
    
    This version uses a weighted scoring system instead of nested conditionals.
    Cyclomatic Complexity: ~5 (GOOD!)
    """
    
    # Calculate weighted total points
    total_points = calculate_total_points(
        score, attendance, assignments_completed, 
        participation, extra_credit, late_submissions,
        group_project_score, midterm_score, final_exam_score
    )
    
    # Apply honors bonus if applicable
    if is_honors_student and total_points >= 90:
        total_points += 2
    
    # Convert to letter grade using simple lookup
    return get_letter_grade(total_points)


def calculate_total_points(score, attendance, assignments_completed,
                          participation, extra_credit, late_submissions,
                          group_project_score, midterm_score, final_exam_score):
    """
    Calculate weighted total points from all components.
    Cyclomatic Complexity: 1 (EXCELLENT!)
    """
    # Weighted scoring system
    points = (
        score * 0.40 +                              # 40% - Main score
        attendance * 0.10 +                         # 10% - Attendance
        (assignments_completed / 20) * 100 * 0.15 + # 15% - Assignments
        participation * 0.10 +                      # 10% - Participation
        group_project_score * 0.10 +                # 10% - Group project
        midterm_score * 0.075 +                     # 7.5% - Midterm
        final_exam_score * 0.075                    # 7.5% - Final exam
    )
    
    # Apply bonuses and penalties
    points += extra_credit
    points -= (late_submissions * 2)  # -2 points per late submission
    
    return points


def get_letter_grade(points):
    """
    Convert numerical points to letter grade.
    Cyclomatic Complexity: 1 (EXCELLENT!)
    """
    # Grade thresholds - simple lookup table
    grade_thresholds = [
        (97, "A+"), (93, "A"), (90, "A-"),
        (87, "B+"), (83, "B"), (80, "B-"),
        (77, "C+"), (73, "C"), (70, "C-"),
        (67, "D+"), (63, "D"), (60, "D-"),
        (0, "F")
    ]
    
    for threshold, grade in grade_thresholds:
        if points >= threshold:
            return grade
    
    return "F"


# Example usage
if __name__ == "__main__":
    # Test case 1: Excellent student
    grade = calculate_student_grade(
        score=95, 
        attendance=95, 
        assignments_completed=16,
        participation=90, 
        extra_credit=5, 
        late_submissions=0,
        group_project_score=90, 
        midterm_score=88, 
        final_exam_score=92,
        is_honors_student=True
    )
    print(f"Excellent student grade: {grade}")
    
    # Test case 2: Average student
    grade = calculate_student_grade(
        score=75, 
        attendance=80, 
        assignments_completed=13,
        participation=70, 
        extra_credit=0, 
        late_submissions=2,
        group_project_score=75, 
        midterm_score=72, 
        final_exam_score=78,
        is_honors_student=False
    )
    print(f"Average student grade: {grade}")
    
    # Test case 3: Struggling student
    grade = calculate_student_grade(
        score=62, 
        attendance=65, 
        assignments_completed=10,
        participation=55, 
        extra_credit=3, 
        late_submissions=5,
        group_project_score=68, 
        midterm_score=60, 
        final_exam_score=65,
        is_honors_student=False
    )
    print(f"Struggling student grade: {grade}")
