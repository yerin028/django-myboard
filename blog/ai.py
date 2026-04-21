from openai import AzureOpenAI
from django.conf import settings

def ask_ai(prompt):
    # 1. 클라이언트 설정 (설정값은 settings.py에서 가져옴)
    client = AzureOpenAI(
        api_version="2025-01-01-preview", 
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_API_KEY
    )

    try:
        # 2. AI 호출
        response = client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {
                    "role": "system",
                    "content": "너는 게시판 도우미야. 내용 요약을 해줘.",
                },
                {
                    "role": "user",
                    "content": prompt, 
                }
            ],
            max_tokens=300, # 답변 길이 제한
            temperature=1.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # 3. 터미널 로그 출력 
        print("\n--- AI 응답 성공 ---")
        print(response.choices[0].message.content)
        print("-------------------\n")

        # 4. 최종 답변 반환
        return response.choices[0].message.content

    except Exception as e:
        # 에러 발생 시 터미널에 상세 내용 출력
        print(f"\n AI 호출 중 에러 발생: {str(e)}\n")
        raise e

