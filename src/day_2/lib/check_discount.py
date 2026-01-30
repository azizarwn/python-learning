# this one naming is noun, better version calculate_discount 
def total_aft_discont(price, discount):
    final_price = price - discount
    return final_price

# this one naming is verb 
def get_payment_status(final_price, discount):
    if final_price <= 0:
        return "your shopping is free!"
    elif final_price == discount:
        return f"pays half price ${final_price}."
    else:
        return f"pays {final_price}."

# here method functions library that can use commonlly
# function naming will be better if it's Verb
# function will use 'return' to return value,