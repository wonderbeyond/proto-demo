import datetime as dt

from dateutil import tz
from google.protobuf.timestamp_pb2 import Timestamp

import demo_pb2 as origin_pb2
import better_pb2.demo as better_pb2

if __name__ == '__main__':
    now = dt.datetime.now(tz=tz.UTC)
    zero_time = dt.datetime.fromtimestamp(0, tz.UTC)

    now_ts = Timestamp()
    now_ts.FromDatetime(now)

    zero_time_ts = Timestamp()
    zero_time_ts.FromDatetime(zero_time)

    # Test case 1: OK
    o1 = origin_pb2.Project(id=1, name="project-001", created_time=now_ts)
    o2 = better_pb2.Project(id=1, name="project-001", created_time=now)
    is_eq = o1.SerializeToString() == o2.SerializeToString()
    print(f'Case 1: {is_eq and "OK" or "Failed"}')

    # Test case 2: OK
    o1 = origin_pb2.Project(id=1, name="project-001", created_time=None)
    o2 = origin_pb2.Project(id=1, name="project-001")
    o3 = better_pb2.Project(id=1, name="project-001", created_time=None)
    o4 = better_pb2.Project(id=1, name="project-001")
    is_eq = o1.SerializeToString() == o2.SerializeToString() == o3.SerializeToString() == o4.SerializeToString()
    print(f'Case 2: {is_eq and "OK" or "Failed"}')

    # Test case 3: Failed
    o1 = origin_pb2.Project(id=1, name="project-001", created_time=zero_time_ts)
    o2 = better_pb2.Project(id=1, name="project-001", created_time=zero_time)
    is_eq = o1.SerializeToString() == o2.SerializeToString()
    print(f'Case 3: {is_eq and "OK" or "Failed"}')
