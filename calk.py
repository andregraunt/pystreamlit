
import streamlit as st

st.title("Калькулятор")

a = st.number_input("Введите первое число", value=0)
b = st.number_input("Введите второе число", value=0)
operation = st.selectbox("Выберите операцию", ["+", "-", "*", "/"])

if st.button("Посчитать"):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/" and b != 0:
        result = a / b
    else:
        result = "Ошибка: деление на ноль!"
    st.write(f"Результат: {result}")