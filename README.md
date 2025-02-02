# 📊 Web Scraping, Crawling, and Data Analysis for Museums

## 📝 Description

This project is a **web scraping and data analysis tool** that extracts, processes, and visualizes specific data labels using various Python libraries efficiently. It includes:
- **Web Scraping** functionalities extracting the following labels that could be changed as desired: [ Person, Date, Place, City, Country].
- **Generates Insights in CSV Files** including the number of occurrences for each entity, this is applicable for a single web page, or a full website.
- **Word Cloud Generation** from the CSV files, where word clouds images are created based on the occurrences.
- **Network Graph Visualization** to represent relationships between entities with two types of graphs, interactive and static graphs.
- **For Both English and Arabic Languages** using language-specific processing techniques. For Arabic, the accuracy of entities extraction is lower due to limitations in GLiNER.

---

## 🚀 Features

✅ Web scraping using `requests` and `BeautifulSoup`

✅ URL processing with `urllib.parse`

✅ Data processing with `pandas`

✅ Word cloud visualization with `wordcloud`

✅ Arabic text reshaping with `arabic-reshaper` and `python-bidi`

✅ Network graph generation with `networkx` and [`d3graph`](https://erdogant.github.io/d3graph/pages/html/index.html)

✅ Named entity recognition with [`GLiNER`](https://github.com/urchade/GLiNER)

---

## 🔧 Installation

### Prerequisites
Ensure you have Python installed on your system. Install the required dependencies using:

```sh
pip install -r requirements.txt
```

---

## 📌 Usage

### 1️⃣ Run the main.py:
```sh
python main.py
```

### 2️⃣ Enter your prefered choices:
![image](https://github.com/user-attachments/assets/51639781-a30c-48f9-89a0-8bfa4ec58e5e)


### 3️⃣ Utilize the outputs and visualizations (word clouds and network graphs):
![image](https://github.com/user-attachments/assets/955250a6-545e-4f65-9afd-a8c17e248636)

![image](https://github.com/user-attachments/assets/184a1f79-6dd7-427c-8dec-52d3258d25a8)


---

## 📂 File Structure

```
├── main.py                      # Main
├── scrapper_v2.py               # Web scraper and Data processing
├── finalCrawling.py             # Web crawling
├── finalMapping_v2.py           # Nationality and country detection and mapping
├── graphs.py                    # Graphs generator
├── finalWordCloud.py            # Word cloud generator
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
├── Amiri-Regular.ttf            # Font for word cloud
├── DejaVuSans.ttf               # Font for word cloud
├── countries_and_demonyms.csv   # Important data for finalMapping_v2.py 
```

---

## 🤝 Contributing
Feel free to **submit issues** or **pull requests** for improvements! We welcome contributions to enhance this project.

---

## 📢 Declaration

This project was developed by **interns** and utilizes **open-source libraries** and existing tools. We acknowledge and appreciate the efforts of the open-source community in making these resources available.

### Contributors:
*[Leen Koree](https://github.com/Leen-QM)* AND *[AlDanah AlAnazi](https://github.com/AlDanah-QM)*

---

🔗 **Happy Coding!** 🚀
