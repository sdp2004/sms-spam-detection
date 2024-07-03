{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.10.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[{"sourceId":982,"sourceType":"datasetVersion","datasetId":483}],"dockerImageVersionId":30732,"isInternetEnabled":false,"language":"python","sourceType":"notebook","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# This Python 3 environment comes with many helpful analytics libraries installed\n# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n# For example, here's several helpful packages to load\n\nimport numpy as np # linear algebra\nimport pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.feature_extraction.text import CountVectorizer\nfrom sklearn.metrics import accuracy_score\nfrom sklearn.metrics import classification_report,confusion_matrix\nfrom sklearn.naive_bayes import MultinomialNB\n# Input data files are available in the read-only \"../input/\" directory\n# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n\nimport os\nfor dirname, _, filenames in os.walk('/kaggle/input'):\n    for filename in filenames:\n        print(os.path.join(dirname, filename))\n\n# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","execution":{"iopub.status.busy":"2024-07-03T15:02:57.725398Z","iopub.execute_input":"2024-07-03T15:02:57.725875Z","iopub.status.idle":"2024-07-03T15:02:57.738364Z","shell.execute_reply.started":"2024-07-03T15:02:57.725844Z","shell.execute_reply":"2024-07-03T15:02:57.737023Z"},"trusted":true},"execution_count":9,"outputs":[{"name":"stdout","text":"/kaggle/input/sms-spam-collection-dataset/spam.csv\n","output_type":"stream"}]},{"cell_type":"code","source":"data=pd.read_csv('/kaggle/input/sms-spam-collection-dataset/spam.csv',encoding='ISO-8859-1',)\n\ndata=data.drop(data.iloc[0:,2:],axis=1)\ndata.head(10)","metadata":{"execution":{"iopub.status.busy":"2024-07-03T15:14:47.605473Z","iopub.execute_input":"2024-07-03T15:14:47.605894Z","iopub.status.idle":"2024-07-03T15:14:47.639634Z","shell.execute_reply.started":"2024-07-03T15:14:47.605864Z","shell.execute_reply":"2024-07-03T15:14:47.638339Z"},"trusted":true},"execution_count":21,"outputs":[{"execution_count":21,"output_type":"execute_result","data":{"text/plain":"     v1                                                 v2\n0   ham  Go until jurong point, crazy.. Available only ...\n1   ham                      Ok lar... Joking wif u oni...\n2  spam  Free entry in 2 a wkly comp to win FA Cup fina...\n3   ham  U dun say so early hor... U c already then say...\n4   ham  Nah I don't think he goes to usf, he lives aro...\n5  spam  FreeMsg Hey there darling it's been 3 week's n...\n6   ham  Even my brother is not like to speak with me. ...\n7   ham  As per your request 'Melle Melle (Oru Minnamin...\n8  spam  WINNER!! As a valued network customer you have...\n9  spam  Had your mobile 11 months or more? U R entitle...","text/html":"<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>v1</th>\n      <th>v2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>ham</td>\n      <td>Go until jurong point, crazy.. Available only ...</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>ham</td>\n      <td>Ok lar... Joking wif u oni...</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>spam</td>\n      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>ham</td>\n      <td>U dun say so early hor... U c already then say...</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>ham</td>\n      <td>Nah I don't think he goes to usf, he lives aro...</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>spam</td>\n      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>ham</td>\n      <td>Even my brother is not like to speak with me. ...</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>ham</td>\n      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>spam</td>\n      <td>WINNER!! As a valued network customer you have...</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>spam</td>\n      <td>Had your mobile 11 months or more? U R entitle...</td>\n    </tr>\n  </tbody>\n</table>\n</div>"},"metadata":{}}]}]}