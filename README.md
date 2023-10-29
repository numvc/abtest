## AB test task

The task was divided into two parts:
1. `ws.py` uses for collecting data from 5 webosckets using `asynio`. It stores data in `pickle_data.pkl` file;
2. `data_analyze.ipynb` reads data from `pickle_data.pkl` file and analyzes via pandas, scipy and matplotlib.

### Before running app:
```
pip install -r requirements.txt
```
### To run:
1. Run `ws.py` as python script;
2. Launch cells in `data_analyze.ipynb`.