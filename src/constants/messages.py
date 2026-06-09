from src.utils.config import get_locale


UI_COPY = {
    "en-US": {
        "nav.chats": "Chats",
        "nav.tools": "Tools",
        "nav.agents": "Agents",
        "nav.search": "Search",
        "nav.new_chat": "New chat",
        "nav.my_agents": "My agents",
        "actions.create": "Create",
        "actions.logout": "Log out",
        "actions.send": "Send",
        "actions.close": "Close",
        "actions.upload_file": "Upload file",
        "actions.image_generate": "Image generation",
        "actions.ppt_generate": "PPT generation",
        "actions.web_search": "Web search",
        "actions.next": "Next",
        "actions.reset_inputs": "Reset inputs",
        "actions.add_student": "Add student",
        "actions.upload_student_excel": "Upload student Excel",
        "actions.download_result": "Get generated result",
        "actions.chat_builder": "Create with chat",
        "actions.form_builder": "Create with settings",
        "fields.search": "Search",
        "fields.message_input": "Type a message.",
        "fields.student_name_search": "Search student name",
        "fields.school_level": "School level",
        "fields.grade": "Grade",
        "fields.subject": "Subject",
        "fields.unit": "Unit",
        "values.elementary_school": "Elementary school",
        "values.middle_school": "Middle school",
        "values.high_school": "High school",
        "tools.quiz": "Quiz Generation",
        "tools.lesson_plan": "Lesson Plan",
        "tools.student_record": "Detailed Student Remarks",
        "tools.student_info": "Student Info",
        "tools.behavior": "Behavior and Overall Opinion",
        "tools.ppt": "PPT Generation",
        "tools.deep_investigation": "Deep Investigation",
        "errors.login.invalid_credentials": "Email or password does not match",
        "errors.login.invalid_email": "Invalid email format.",
    },
    "ko-KR": {
        "nav.chats": "채팅",
        "nav.tools": "도구",
        "nav.agents": "에이전트",
        "nav.search": "검색",
        "nav.new_chat": "새 대화",
        "nav.my_agents": "내 에이전트",
        "actions.create": "만들기",
        "actions.logout": "로그아웃",
        "actions.send": "보내기",
        "actions.close": "닫기",
        "actions.upload_file": "파일 업로드",
        "actions.image_generate": "이미지 생성",
        "actions.ppt_generate": "PPT 생성",
        "actions.web_search": "웹 검색",
        "actions.next": "다음으로",
        "actions.reset_inputs": "입력 내역 초기화",
        "actions.add_student": "학생 추가",
        "actions.upload_student_excel": "학생 정보 엑셀 업로드",
        "actions.download_result": "생성 결과 받기",
        "actions.chat_builder": "대화로 만들기",
        "actions.form_builder": "설정으로 생성",
        "fields.search": "검색",
        "fields.message_input": "메시지를 입력해 주세요.",
        "fields.student_name_search": "학생 이름 검색",
        "fields.school_level": "학교급",
        "fields.grade": "학년",
        "fields.subject": "과목",
        "fields.unit": "단원",
        "values.elementary_school": "초등학교",
        "values.middle_school": "중학교",
        "values.high_school": "고등학교",
        "tools.quiz": "퀴즈 생성",
        "tools.lesson_plan": "수업지도안",
        "tools.student_record": "세부 특기사항",
        "tools.student_info": "학생 정보",
        "tools.behavior": "행동특성 및 종합의견",
        "tools.ppt": "PPT 생성",
        "tools.deep_investigation": "심층 조사",
        "errors.login.invalid_credentials": "이메일 또는 비밀번호가 일치하지 않습니다",
        "errors.login.invalid_email": "이메일 형식이 올바르지 않습니다.",
    },
}


def get_message(key, locale=None):
    locale = locale or get_locale()
    locale_messages = UI_COPY.get(locale, {})
    if key in locale_messages:
        return locale_messages[key]
    return UI_COPY["en-US"].get(key, key)


def get_message_candidates(key, locale=None):
    locale = locale or get_locale()
    candidates = []
    localized = UI_COPY.get(locale, {}).get(key)
    english = UI_COPY["en-US"].get(key)

    for value in (localized, english):
        if value and value not in candidates:
            candidates.append(value)

    for locale_messages in UI_COPY.values():
        value = locale_messages.get(key)
        if value and value not in candidates:
            candidates.append(value)

    return candidates or [key]


LOGIN_ERROR_MESSAGE = get_message("errors.login.invalid_credentials")
