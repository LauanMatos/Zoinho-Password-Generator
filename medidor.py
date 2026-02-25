def medir_forca(tamanho):
    """Classifica a força da senha baseada no tamanho"""
    if tamanho < 11:
        return "Weak"
    elif tamanho < 21:
        return "Medium"
    elif tamanho < 31:
        return "Strong"
    else:
        return "Very Strong"