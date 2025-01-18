#Task 7: Voting Eligibility

def voting_eligibility(age,is_citizen):
    if is_citizen=="yes":
        is_citizen=True
    else:
        is_citizen=False
        
    if(age>=18 and is_citizen):
        print("Eligible for vote")
    else:
        print("not eligible for vote")
    
voting_eligibility(int(input("Enter your age:")),str(input("Are you citizen?(yes/no):")))