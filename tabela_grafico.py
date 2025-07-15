import pandas as pd
import matplotlib.pyplot as plt

table = pd.DataFrame({
    'Idade' : [20, 23, 65, 57, 52],
    'Nome' : ['Leonardo', 'Adriano', 'João', 'Maria', 'José']
})

plt.hist(table['Idade'])