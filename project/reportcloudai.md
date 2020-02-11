# Cloud AI Services Azure and Oracle

Harsha Upadhyay, [fa19-516-147](https://github.com/cloudmesh-community/fa19-516-147/edit/master/project/report.md)

[Contributors](https://github.com/cloudmesh-community/fa19-516-147/graphs/contributors)

[Insights](https://github.com/cloudmesh-community/fa19-516-147/pulse)
 
Cloud AI Services 

## Azure AI

Azure machine learning is a cloud-based environment which can be used for machine learning project purposes. Azure AI can be used for train, deploy, automate, manage, and track ML models and compatible with open-source tools like  PyTorch, TensorFlow, and scikit-learn.

Azure offers AI services through Azure Cognitive services which include APIs, SDKs, and services to help developers build AI applications.

### Microsoft Azure Machine Learning Studio

This is UI based environment to develop machine learning application with no or low use of code. Azure Studio has a drag and drop UI feature to help user to built machine learning application without getting into coding complexity.

### Azure Machine Learning SDK for Python

Azure MAchine Learning SDK for python is for Data scientists and AI developers to built and run machine learning using Python. This uses Microsoft Machine Learning Services. 
There are two type of install avilable with Azure AI SDK : Default install & Advanced install.

To install SDK pip command on command can be used.

Default : pip install --upgrade azureml-sdk

Advanced : pip install --upgrade azureml-sdk[explain,automl]

The native package structure which installed via the azureml-sdk package are:

azureml-sdk
azureml-core
azureml-dataprep
azureml-train
azureml-train-core
azureml-pipeline
azureml-pipeline-core
azureml-pipeline-steps

Complete detail on Installation & Packages <https://docs.microsoft.com/en-us/python/api/overview/azureml-sdk/install?view=azure-ml-py>

### Azure AI APIs

<https://docs.microsoft.com/en-us/azure/cognitive-services/welcome>

Example using Azure AI API with Python 
<https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/text-analytics-sdk?pivots=programming-language-python&tabs=version-3#sentiment-analysis>

## Oracle AI

### Oracle Machine Learning for Python

Oracle offers machine learning function in the database.
Oracle machine learning for python called as OML4PY is a part of Oracle Advanced Analytics option which introduces automated model selection via hyperparameter tuning and automated feature selection to enhance model accuracy and performance.

pip install oml4py

## References

1. Azure Cognitive Services <https://docs.microsoft.com/en-us/azure/cognitive-services/welcome>
1. Azure AI SDK <https://docs.microsoft.com/en-us/python/api/overview/azureml-sdk/install?view=azure-ml-py>
1. Sentiment Analysis with Azure AI <https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/text-analytics-sdk?pivots=programming-language-python&tabs=version-3#sentiment-analysis>
1. Azure AI Documentaion <https://docs.microsoft.com/en-us/azure/machine-learning/>
1. OML4PY <https://towardsdatascience.com/oracle-machine-learning-for-python-e335fc0a50e8>
1. Oracle AI API Architecture <https://docs.oracle.com/en/solutions/connect-your-bot-to-ml-api/index.html#GUID-FA624926-1883-467C-A08D-6588D329B95C>
1. Oracle Machine Learning for Python <https://towardsdatascience.com/oracle-machine-learning-for-python-e335fc0a50e8>
