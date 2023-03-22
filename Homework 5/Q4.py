def prob_loaded_given_all_heads():
    probability_b_given_a = (1/2)**5
    p_a = 0.9
    probability_b_given_not_a = (9/10)**4 * (1/10)
    probability_not_a = 0.1
    probability_b = probability_b_given_a*p_a + probability_b_given_not_a*probability_not_a
    return probability_b_given_not_a*probability_not_a / probability_b

print(prob_loaded_given_all_heads())