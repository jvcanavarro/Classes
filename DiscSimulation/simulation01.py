import statistics as st


filename = "entrada-lista-1.txt"
data = open(filename, "r").read().split(',')
int_data = list(map(float, data))


print(st.quantiles(int_data))

q1 = (st.quantiles(int_data))[0]
print(round(q1, 4))

q2 = (st.quantiles(int_data))[1]
print(round(q2, 4))

q3 = (st.quantiles(int_data))[2]
print(round(q3, 4))

# mediana
print(round(st.median(int_data), 4))

# amplitude
print(round(max(int_data) - min(int_data), 4))

# variancia
print(round(st.variance(int_data), 4))

# desvio padrão
print(round(st.stdev(int_data), 4))
