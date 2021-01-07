import aws_lambda_typing as lambda_typing


def test_code_pipeline_event() -> None:
    dummy: lambda_typing.CodePipelineEvent = {
        "CodePipeline.job": {
            "id": "c0d76431-b0e7-xmpl-97e3-e8ee786eb6f6",
            "accountId": "123456789012",
            "data": {
                "actionConfiguration": {
                    "configuration": {
                        "FunctionName": "my-function",
                        "UserParameters": "{\"KEY\": \"VALUE\"}"
                    }
                },
                "inputArtifacts": [
                    {
                        "name": "my-pipeline-SourceArtifact",
                        "revision": "e0c7xmpl2308ca3071aa7bab414de234ab52eea",
                        "location": {
                            "type": "S3",
                            "s3Location": {
                                "bucketName": "us-west-2-123456789012-my-pipeline",
                                "objectKey": "my-pipeline/test-api-2/TdOSFRV"
                            }
                        }
                    }
                ],
                "outputArtifacts": [
                    {
                        "name": "invokeOutput",
                        "revision": None,
                        "location": {
                            "type": "S3",
                            "s3Location": {
                                "bucketName": "us-west-2-123456789012-my-pipeline",
                                "objectKey": "my-pipeline/invokeOutp/D0YHsJn"
                            }
                        }
                    }
                ],
                "artifactCredentials": {
                    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                    "secretAccessKey": "6CGtmAa3lzWtV7a...",
                    "sessionToken": "IQoJb3JpZ2luX2VjEA...",
                    "expirationTime": 1575493418000
                }
            }
        }
    }
