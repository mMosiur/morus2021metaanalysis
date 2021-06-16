#%% Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%% Setup variables
# Set destination folder for the output
output_dir = "Plots/"
MEDIAN_COLOR = "#5B7EBD"
ALL_MEDIAN_COLOR = "#0000CC"
MEAN_COLOR = "#EE854A"
ALL_MEAN_COLOR = "#CC0000"
if output_dir != "" and not output_dir.endswith("/"):
    output_dir += "/"

#%% Define plotting function
def plot_to_file(filename, xlabel, labels, means, medians, overall_mean, overall_median, x_tick_rotation=0):
    plt.xlabel(xlabel, fontsize="large")
    plt.ylabel("Ilość wyświetleń na dzień", fontsize="large")
    if x_tick_rotation > 0:
        plt.xticks(rotation=x_tick_rotation)
    plt.bar(labels, means, label="Średnia podzbioru", color=MEAN_COLOR)
    plt.bar(labels, medians, label="Mediana podzbioru", color=MEDIAN_COLOR)
    plt.axhline(y=overall_mean, label="Średnia ogólna", linestyle="dashed", color=ALL_MEAN_COLOR)
    plt.axhline(y=overall_median, label="Mediana ogólna", linestyle="dotted", color=ALL_MEDIAN_COLOR)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


#%% Generate area plt
plotname = "Area"
labels = [
    "Biznes",
    "Społeczne",
    "Życie",
    "Komputer",
    "Fizyczne"
]
web_hits_per_day_means = [
    97.5026251466547,
    61.1283855315268,
    46.6719117823716,
    40.7990616728854,
    39.1768414327089
]
web_hits_per_day_medians = [
    68.3113043478261,
    28.0968992248062,
    29.8797767282095,
    28.6781651376147,
    24.0927460092948
]
overall_mean = 48.0151966575709
overall_median = 29.4331527591751
plot_to_file(
    output_dir+plotname+".pdf",
	"Dziedzina",
    labels,
    web_hits_per_day_means,
    web_hits_per_day_medians,
    overall_mean,
    overall_median
)

# %% Generate associated tasks plot
plotname = "AssociatedTasks"
labels = [
    "Regresja",
    "Klasteryzacja",
    "Klasyfikacja",
    "Analiza przyczynowa"
]
web_hits_per_day_means = [
    60.8208282923251,
    57.5518400453074,
    47.4435706879225,
    43.9305695604709
]
web_hits_per_day_medians = [
    42.0281437125749,
    38.2255683546754,
    29.4000559666687,
    24.8001854197506
]
overall_mean = 47.8447186857058
overall_median = 29.7893674150147
plot_to_file(
    output_dir+plotname+".pdf",
	"Powiązane zadania",
    labels,
    web_hits_per_day_means,
    web_hits_per_day_medians,
    overall_mean,
    overall_median
)

# %% Generate attribute characteristics plot
plotname = "AttributeCharacteristics"
labels = [
    "Rzeczywiste",
    "Całkowite",
    "Kategorialne"
]
web_hits_per_day_means = [
    52.4213793303745,
    49.0239619294068,
    27.8513493750351
]
web_hits_per_day_medians = [
    32.7393798449612,
    28.9011627906977,
    16.8981441519206
]
overall_mean = 47.7484250089279
overall_median = 29.5409562727882
plot_to_file(
    output_dir+plotname+".pdf",
	"Cechy atrybutów",
    labels,
    web_hits_per_day_means,
    web_hits_per_day_medians,
    overall_mean,
    overall_median
)

# %% Generate data set characteristics
plotname = "DataSetCharacteristics"
labels = [
    "Szeregi czasowe",
    "Jednowymiarowe",
    "Wielowymiarowe",
    "Sekwencyjne",
    "Tekstowe",
    "Teorie domenowe"
]
web_hits_per_day_means = [
    61.2964009809620,
    50.8545878809314,
    49.7219830647435,
    44.9979290224581,
    37.2563425344624,
    28.7873251485220
]
web_hits_per_day_medians = [
    36.1556072953046,
    31.1440015568176,
    29.8434876210980,
    29.1660219774022,
    25.8350659191781,
    18.5250873149915
]
overall_mean = 46.3988901141464
overall_median = 28.9655858084115
plot_to_file(
    output_dir+plotname+".pdf",
	"Cechy zbioru danych",
    labels,
    web_hits_per_day_means,
    web_hits_per_day_medians,
    overall_mean,
    overall_median,
    x_tick_rotation=10
)

# %% Generate missing values plot
plotname = "MissingValues"
labels = [
    "Tak",
    "Nie"
]
web_hits_per_day_means = [
    49.3893245295069,
    29.8110445027449
]
web_hits_per_day_medians = [
    32.0568887958992,
    16.2583589372854
]
overall_mean = 42.0871552222281
overall_median = 26.4095238095238
plot_to_file(
    output_dir+plotname+".pdf",
	"Brakujące dane",
    labels,
    web_hits_per_day_means,
    web_hits_per_day_medians,
    overall_mean,
    overall_median
)
