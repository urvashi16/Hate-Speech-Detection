def combine(t_model, l_model, f_model):
    t_model = not t_model
    l_model = not l_model
    L = ["Traditional Model" if t_model else "", "LSTM Model" if l_model else "", "Fusion Model" if f_model else ""]
    final_message = "The message has been flagged as hateful by " + ", ".join([str(i + 1) + ": " + str(v) for i, v in enumerate(sorted(L, reverse = True)) if v])
    
    isHate = any(L)

    return isHate, final_message
