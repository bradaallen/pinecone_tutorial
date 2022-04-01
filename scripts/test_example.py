
from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType, FileSource
import os
import platform

path = os.getcwd() + "/data/test_questions.parquet"
source = FileSource(
            path= path if platform.system() != 'Windows' else path.replace('/', '\\'),
                event_timestamp_column="datetime",
                    created_timestamp_column="created",
                    )

test_question = Entity(name="qid", value_type=ValueType.INT64, description="question id",)

question_feature = Feature(
            name="question1",
                dtype=ValueType.STRING
                )

embedding_features = [
                Feature(name=f"e_{i}", dtype=ValueType.FLOAT)
                        for i in range(384)
                              ]

test_questions_view = FeatureView(
            name="test_questions",
                entities=["qid"],
                    ttl=Duration(seconds=86400 * 1),
                        features= [question_feature, *embedding_features],
                            online=True,
                                input=source,
                                    tags={},
                                    )
