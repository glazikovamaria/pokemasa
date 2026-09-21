import seaborn as sns
from matplotlib import pyplot as plt



def num_dist(data, var: list):
    """
    Функция построения числовой дистограммы.

    :param data: данные
    :param var: параметры, которые включаем в диаграмму
    """
    fig, ax = plt.subplots(1, 2, figsize=(20, 4))
    
    sns.histplot(data=data, x=var, kde=True, ax=ax[0])
    sns.boxplot(data=data, x=var, ax=ax[1])
    ax[0].set_title(f"{var} Distribution Histogram")
    ax[1].set_title(f"{var} Distribution Boxplot")

    plt.show()



def cat_dist(data, var: list):
    """
    Функция построения категорийной дистограммы.

    :param data: данные
    :param var: параметры, которые включаем в диаграмму
    """
    fig, ax = plt.subplots(1, 2, figsize=(20, 4))

    data[var].value_counts().sort_values(ascending=False).plot(kind="pie", explode=[0.05 for _ in data[var].dropna().unique()], autopct='%1.1f%%', ax=ax[0], shadow=True)
    ax[0].set_title(f"{var} Pie Chart")
    ax[0].set_ylabel('')
   
    count = sns.countplot(x=var, data=data, order=data[var].value_counts().sort_values(ascending=False).index, ax=ax[1])
    for bar in count.patches:
        count.annotate(format(bar.get_height()),
            (bar.get_x() + bar.get_width() / 2,
            bar.get_height()), ha='center', va='center',
            size=10, xytext=(0, 2),
            textcoords='offset points')
    ax[1].set_title(f"{var} Bar Chart")
    ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
    plt.show()