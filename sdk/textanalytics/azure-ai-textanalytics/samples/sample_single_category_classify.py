# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_single_category_classify.py

DESCRIPTION:
    This sample demonstrates how to classify documents into a single custom category. For example,
    movie plot summaries can be categorized into a single movie genre like "Mystery", "Drama", "Thriller",
    "Comedy", "Action", etc. Classifying documents is available as an action type through
    the begin_analyze_actions API.

    For information on regional support of custom features and how to train a model to
    classify your documents, see https://aka.ms/azsdk/textanalytics/customfunctionalities

USAGE:
    python sample_single_category_classify.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your Text Analytics subscription key
    3) SINGLE_CATEGORY_CLASSIFY_PROJECT_NAME - your Text Analytics Language Studio project name
    4) SINGLE_CATEGORY_CLASSIFY_DEPLOYMENT_NAME - your Text Analytics deployed model name
"""


import os


def sample_classify_document_single_category():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        SingleCategoryClassifyAction
    )

    endpoint = os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"]
    key = os.environ["AZURE_TEXT_ANALYTICS_KEY"]
    project_name = os.environ["SINGLE_CATEGORY_CLASSIFY_PROJECT_NAME"]
    deployed_model_name = os.environ["SINGLE_CATEGORY_CLASSIFY_DEPLOYMENT_NAME"]
    path_to_sample_document = os.path.abspath(
        os.path.join(
            os.path.abspath(__file__),
            "..",
            "./text_samples/custom_classify_sample.txt",
        )
    )

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(path_to_sample_document) as fd:
        document = [fd.read()]

    poller = text_analytics_client.begin_analyze_actions(
        document,
        actions=[
            SingleCategoryClassifyAction(
                project_name=project_name,
                deployment_name=deployed_model_name
            ),
        ],
    )

    document_results = poller.result()
    for doc, classification_results in zip(document, document_results):
        for classification_result in classification_results:
            if not classification_result.is_error:
                classification = classification_result.classification
                print("The document text '{}' was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            else:
                print("Document text '{}' has an error with code '{}' and message '{}'".format(
                    doc, classification_result.code, classification_result.message
                ))


if __name__ == "__main__":
    sample_classify_document_single_category()