# -*- coding:utf-8 -*-
# Made by Kei Choi(hanul93@naver.com)


# 악성코드 상태값
NOT_FOUND = 0  # 악성코드 찾지 못함
INFECTED = 1  # 감염
SUSPECT = 2  # 의심
WARNING = 3  # 경고
IDENTIFIED = 4  # 식별
ERROR = 99  # 에러 메시지 처리


# 악성코드 치료 방법
MASTER_IGNORE = 0  # 현재 지원하지 않는 상태이므로 파일을 그대로 둘 것
MASTER_PACK = 1  # 최상위 파일 압축(재구성), mkarc 함수 처리 가능
MASTER_DELETE = 2  # 최상위 파일을 지울 것


# 엔진의 타입
ARCHIVE_ENGINE = 80  # 압축 해제 엔진


# -------------------------------------------------------------------------
# KavMain 클래스
# -------------------------------------------------------------------------
class KavMain:
    # ---------------------------------------------------------------------
    # init(self, plugins_path)
    # 플러그인 엔진을 초기화 한다.
    # 인력값 : plugins_path - 플러그인 엔진의 위치
    #         verbose      - 디버그 모드 (True or False)
    # 리턴값 : 0 - 성공, 0 이외의 값 - 실패
    # ---------------------------------------------------------------------
    def init(self, plugins_path, verbose=False):  # 플러그인 엔진 초기화
        return 0  # 플러그인 엔진 초기화 성공

    # ---------------------------------------------------------------------
    # uninit(self)
    # 플러그인 엔진을 종료한다.
    # 리턴값 : 0 - 성공, 0 이외의 값 - 실패
    # ---------------------------------------------------------------------
    def uninit(self):  # 플러그인 엔진 종료
        return 0  # 플러그인 엔진 종료 성공

    # ---------------------------------------------------------------------
    # getinfo(self)
    # 플러그인 엔진의 주요 정보를 알려준다. (제작자, 버전, ...)
    # 리턴값 : 플러그인 엔진 정보
    # ---------------------------------------------------------------------
    def getinfo(self):  # 플러그인 엔진의 주요 정보
        info = dict()  # 사전형 변수 선언

        info['author'] = 'Kei Choi'  # 제작자
        info['version'] = '1.0'  # 버전
        info['title'] = 'KicomAV Kernel'  # 엔진 설명
        info['kmd_name'] = 'kernel'  # 엔진 파일 이름

        return info