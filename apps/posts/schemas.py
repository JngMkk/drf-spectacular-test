from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter

CREATE_POST_BODY_EX = OpenApiExample(
    "Success Example",
    request_only=True,
    summary="게시물 작성 예시",
    value={"title": "이것은 제목", "name": "이름", "content": "으아아아아아"},
)

LIST_POST_PARAMS = [
    OpenApiParameter(
        "name_param",
        type=OpenApiTypes.STR,
        location=OpenApiParameter.QUERY,
        description="Filter by name",
        examples=[
            OpenApiExample(
                "name query ex", summary="짧은 설명", description="긴 설명", value="이름"
            )
        ],
    )
]
