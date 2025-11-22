from typing import Optional, List, Tuple

def remove_negative_values(notches: List[int]) -> List[int]:
    """마지막 음수 값 뒤에 있는 모든 수 반환, 음수가 없으면 원본 리스트 반환"""
    # 역순으로 탐색해서 마지막 음수 값을 찾음
    for i in range(len(notches) - 1, -1, -1):
        if notches[i] < 0:
            # 마지막 음수 이후의 모든 값들 반환
            return notches[i+1:]
    # 음수가 없으면 원본 리스트 반환
    return notches

def is_stair_pattern(notches: List[int]) -> bool:
        
        notches = remove_negative_values(notches)

        if len(notches) < 5:
            return False

        peak_reached = False
        prev = notches[0]

        for cur in notches[1:]:
            if not peak_reached:
                if cur < prev:  # 내려가기 시작하면 피크 도달
                    peak_reached = True
            else:
                if cur > prev:  # 피크 이후 다시 올라가면 실패
                    return False
            prev = cur

        # 마지막은 1, 2로 끝나야 함
        if notches[-1] not in [1, 2]:
            return False

        return True
print(is_stair_pattern(remove_negative_values([6, 1, 2, 1])))

