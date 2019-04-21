def average(n):
    ave = sum(n)/ len (n)
    return ave
average 
def course_grader(test_scores):
    # Your code here
    if average (test_scores) >= 70:
        #if test_scores > 49:
        return ("pass")
    elif average (test_scores) < 70 and test_scores < 50:
        print( "fail")
    
def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()
