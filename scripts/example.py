from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, ValueType, FileSource
import os
import platform

path = os.getcwd() + "/data/NQ_questions.parquet"
source = FileSource(
            path= path if platform.system() != 'Windows' else path.replace('/', '\\'),
                event_timestamp_column="datetime",
                )

question = Entity(name="qid", value_type=ValueType.INT64)

question_feature = Feature(
            name="question_text",
                dtype=ValueType.STRING
                )

answer_feature = Feature(
            name="document_url",
                dtype=ValueType.STRING
                )

embedding_features = [
                Feature(name=f"e_{i}", dtype=ValueType.FLOAT)
                        for i in range(384)
                              ]

questions_view = FeatureView(
            name="questions",
                entities=["qid"],
                    ttl=Duration(seconds=86400),
                        features= [question_feature, answer_feature, *embedding_features],
                            
                            input=source,
                                
                            )
