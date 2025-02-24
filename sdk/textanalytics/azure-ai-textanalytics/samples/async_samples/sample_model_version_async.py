# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_model_version_async.py

DESCRIPTION:
    This sample demonstrates how to set the model_version for pre-built Text Analytics models.
    Recognize entities is used in this sample, but the concept applies generally to all pre-built Text Analytics models.

    By default, model_version is set to "latest". This indicates that the latest generally available version
    of the model will be used. Model versions are date based, e.g "2021-06-01".
    See the documentation for a list of all model versions:
    https://docs.microsoft.com/azure/cognitive-services/language-service/named-entity-recognition/how-to-call#specify-the-ner-model

USAGE:
    python sample_model_version_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your Text Analytics subscription key
"""

import os
import asyncio


async def sample_model_version_async():
    print("--------------Choosing model_version sample--------------")
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics.aio import TextAnalyticsClient
    from azure.ai.textanalytics import RecognizeEntitiesAction

    endpoint = os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"]
    key = os.environ["AZURE_TEXT_ANALYTICS_KEY"]

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    documents = [
        "I work for Foo Company, and we hired Contoso for our annual founding ceremony. The food \
        was amazing and we all can't say enough good words about the quality and the level of service."
    ]

    async with text_analytics_client:
        print("\nSetting model_version='latest' with recognize_entities")
        result = await text_analytics_client.recognize_entities(documents, model_version="latest")
        result = [review for review in result if not review.is_error]

        print("...Results of Recognize Entities:")
        for review in result:
            for entity in review.entities:
                print(f"......Entity '{entity.text}' has category '{entity.category}'")

        print("\nSetting model_version='latest' with recognize entities action in begin_analyze_actions")
        poller = await text_analytics_client.begin_analyze_actions(
            documents,
            actions=[
                RecognizeEntitiesAction(model_version="latest")
            ]
        )

        print("...Results of Recognize Entities Action:")
        document_results = await poller.result()
        async for action_results in document_results:
            recognize_entities_result = action_results[0]
            if recognize_entities_result.is_error:
                print("......Is an error with code '{}' and message '{}'".format(
                    recognize_entities_result.code, recognize_entities_result.message
                ))
            else:
                for entity in recognize_entities_result.entities:
                    print(f"......Entity '{entity.text}' has category '{entity.category}'")


async def main():
    await sample_model_version_async()


if __name__ == '__main__':
    asyncio.run(main())
