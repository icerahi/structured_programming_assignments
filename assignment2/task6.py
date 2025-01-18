#Task 6: Discount Eligibility

def eligibility_check(original_price):
    discount_amount=0
    final_price=0
    if (original_price>100):
        discount_amount=(10/100)*original_price
        final_price=original_price-discount_amount
        print("Original Price: ",original_price)
        print("Discount Amount:",discount_amount)
        print("Final Price:",final_price)
    else:
        print("not eligible")
        
eligibility_check(float(input("Enter Product price:")))