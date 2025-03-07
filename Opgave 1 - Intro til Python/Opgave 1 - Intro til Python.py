from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import numpy as np

# Liste af navne
names = ["Zander", "Travon", "Juanita", "Trista", "Quinlan", "Franklin", "Tasia", "Bridget", "Kourtney", "Jewel", "Zander", "Trista"]

# Tæl antal navne før fjernelse af dubletter
total_names_count = len(names)

# Fjern duplikater, hvis der er nogen
unique_names = list(set(names))

# Tæl antal dubletter
duplicates_count = total_names_count - len(unique_names)

# Sorter navne alfabetisk og efter længde
names_sorted = sorted(unique_names, key=lambda x: (len(x), x))
print("Navne sorteret alfabetisk og efter længde:", names_sorted[:10])

# Optælling af bogstaver
letter_count = defaultdict(int)
for name in unique_names:
    for letter in name.lower():  # Konverter til små bogstaver for at undgå forskel mellem store/små
        letter_count[letter] += 1

# Udskriv bogstavtælling sorteret efter hyppighed
sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
print("Bogstavoptælling sorteret efter hyppighed:", sorted_letter_count)

# Tæl antal navne i listen
print(f"Antal navne i listen: {total_names_count} (heraf {duplicates_count} dublet{'' if duplicates_count == 1 else 'ter'})")

# Frekvensanalyse: Visualisering af bogstavfrekvens
plt.figure(figsize=(10, 6))
plt.bar(sorted_letter_count.keys(), sorted_letter_count.values(), color='skyblue')
plt.title('Frekvens af bogstaver i navnelisten')
plt.xlabel('Bogstaver')
plt.ylabel('Frekvens')
plt.show()

# Ordsky baseret på bogstavhyppighed
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(sorted_letter_count)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Analyse af navnelængder
name_lengths = [len(name) for name in unique_names]
avg_length = np.mean(name_lengths)
median_length = np.median(name_lengths)
print(f'Gennemsnitlig navnelængde: {avg_length:.2f}')
print(f'Median navnelængde: {median_length}')

# Visualisering af navnelængder
plt.figure(figsize=(10, 6))
sns.histplot(name_lengths, bins=range(min(name_lengths), max(name_lengths) + 1), kde=True)
plt.title('Fordeling af navnelængder')
plt.xlabel('Navnelængde')
plt.ylabel('Antal navne')
plt.show()