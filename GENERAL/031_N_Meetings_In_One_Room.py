"""
https://takeuforward.org/data-structure/n-meetings-in-one-room/
"""

class Solution :
    def maxMeetings(self,
                    meeting_times: list[list[int]]) -> int :
        # sort acc to start time
        meeting_times.sort(key=self.sort_criteria)

        last_meeting_time = 0
        meetings = 0

        for _ in meeting_times :
            if _[0] >= last_meeting_time :
                last_meeting_time = _[1]
                meetings += 1

        return meetings

    def sort_criteria(self, val) :
        return val[0]
