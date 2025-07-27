import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

import tensorflow as tf
import tensorflow_hub as hub

import shap
import lime
import lime.lime_tabular

from tqdm import tqdm
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings("ignore")