#12
import json

def deep_diff(obj1, obj2, path=''):
    diffs = []
    keys = set(obj1.keys()) | set(obj2.keys())
    
    for key in keys:
        full_path = f"{path}.{key}" if path else key
        
        in_obj1 = key in obj1
        in_obj2 = key in obj2
        
        val1 = obj1[key] if in_obj1 else '<missing>'
        val2 = obj2[key] if in_obj2 else '<missing>'
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            diffs.extend(deep_diff(val1, val2, full_path))
        elif val1 != val2:
            # <missing> болса json.dumps қолданбаймыз
            s_val1 = val1 if val1 == '<missing>' else json.dumps(val1, separators=(',', ':'))
            s_val2 = val2 if val2 == '<missing>' else json.dumps(val2, separators=(',', ':'))
            diffs.append(f"{full_path} : {s_val1} -> {s_val2}")
    
    return diffs

# Input
obj1 = json.loads(input())
obj2 = json.loads(input())

# Compute differences
differences = deep_diff(obj1, obj2)

# Output
if differences:
    for line in sorted(differences):
        print(line)
else:
    print("No differences")

#13
import json
import re
import sys

def resolve_query(data, query):
    # Сұранысты бөлшектеу: нүктелер мен жақшаларды бөліп аламыз
    # Мысалы: "user.friends[2].name" -> ['user', 'friends', '2', 'name']
    tokens = re.findall(r'[^.\[\]]+', query)
    
    current = data
    try:
        for token in tokens:
            if isinstance(current, list):
                # Егер қазіргі нысан тізім болса, индексті санға айналдырамыз
                index = int(token)
                if index < 0 or index >= len(current):
                    return "NOT_FOUND"
                current = current[index]
            elif isinstance(current, dict):
                # Егер нысан сөздік болса, кілтті тексереміз
                if token not in current:
                    return "NOT_FOUND"
                current = current[token]
            else:
                # Егер ары қарай жол бар, бірақ нысан қарапайым тип болса
                return "NOT_FOUND"
        
        # Нәтижені JSON форматында (бос орынсыз) шығару
        return json.dumps(current, separators=(',', ':'))
    except (ValueError, TypeError, IndexError):
        return "NOT_FOUND"

def main():
    # Барлық енгізуді оқу
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # 1. JSON-ды оқу
    try:
        json_obj = json.loads(input_data[0])
    except:
        return

    # 2. Сұраныстар санын оқу
    if len(input_data) < 2:
        return
    q_count = int(input_data[1])

    # 3. Әр сұранысты өңдеу
    for i in range(2, 2 + q_count):
        if i < len(input_data):
            query = input_data[i].strip()
            print(resolve_query(json_obj, query))

if __name__ == "__main__":
    main()

#14
import sys
from datetime import datetime, timedelta, timezone

def parse_date(date_str):
    # Жолды бөліктерге бөлу: "2025-01-01" және "UTC+03:00"
    parts = date_str.strip().split(' ')
    date_part = parts[0]
    tz_part = parts[1] # Мысалы: UTC+03:00 немесе UTC-05:00
    
    # Жыл, ай, күнді алу
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    # Уақыт белдеуін өңдеу (UTC+HH:MM немесе UTC-HH:MM)
    sign = 1 if tz_part[3] == '+' else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])
    
    # Offset-ті жасау (UTC белдеуінен қаншалықты алшақ екені)
    offset = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
    
    # Уақытты түн ортасы 00:00 және берілген уақыт белдеуімен қайтару
    return dt.replace(tzinfo=offset)

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
        
    # Екі күнді оқып, UTC форматына келтіру
    dt1 = parse_date(lines[0])
    dt2 = parse_date(lines[1])
    
    # Айырмашылықты секундпен алып, тәулікке бөлу
    diff_seconds = abs((dt1 - dt2).total_seconds())
    days = int(diff_seconds // 86400)
    
    print(days)

if __name__ == "__main__":
    solve()

#15
from datetime import datetime, timedelta
import math

def parse_datetime(s):
    # Split "YYYY-MM-DD" and "UTC+/-HH:MM"
    parts = s.split()
    date_str = parts[0]
    offset_str = parts[1].replace('UTC', '')
    
    # Calculate offset in seconds
    sign = 1 if offset_str[0] == '+' else -1
    h, m = map(int, offset_str[1:].split(':'))
    offset_seconds = sign * (h * 3600 + m * 60)
    
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    # UTC timestamp = Local midnight - offset
    return dt.timestamp() - offset_seconds, dt, offset_seconds

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_birthday_timestamp(b_month, b_day, target_year, b_offset):
    # Handle Feb 29 rule
    m, d = b_month, b_day
    if m == 2 and d == 29 and not is_leap(target_year):
        d = 28
    
    dt = datetime(target_year, m, d)
    return dt.timestamp() - b_offset

# Main Logic
def solve():
    line1 = input().strip() # Birth
    line2 = input().strip() # Current
    
    _, birth_dt, b_offset = parse_datetime(line1)
    curr_utc, curr_dt, _ = parse_datetime(line2)
    
    b_month, b_day = birth_dt.month, birth_dt.day
    
    # Check current year birthday
    t1 = get_birthday_timestamp(b_month, b_day, curr_dt.year, b_offset)
    
    if t1 >= curr_utc:
        target_utc = t1
    else:
        # Check next year birthday
        target_utc = get_birthday_timestamp(b_month, b_day, curr_dt.year + 1, b_offset)
        
    diff_seconds = target_utc - curr_utc
    print(math.ceil(diff_seconds / 86400))

solve()




#16
import sys
from datetime import datetime, timedelta, timezone

def parse_to_utc(line):
    # Жолды бөліктерге бөлу: "2026-01-01", "10:00:00", "UTC+03:00"
    parts = line.strip().split()
    if len(parts) < 3:
        return None
    
    date_time_str = f"{parts[0]} {parts[1]}"
    tz_str = parts[2] # UTC+HH:MM немесе UTC-HH:MM
    
    # 1. Уақытты оқу (белдеусіз)
    dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    
    # 2. Уақыт белдеуінің офсетін (ығысуын) есептеу
    # UTC+HH:MM форматынан белгіні, сағатты және минутты алу
    sign = 1 if tz_str[3] == '+' else -1
    h_offset = int(tz_str[4:6])
    m_offset = int(tz_str[7:9])
    
    # 3. Офсетті қолдана отырып, уақыт белдеуі бар нысан жасау
    tz = timezone(timedelta(hours=sign * h_offset, minutes=sign * m_offset))
    return dt.replace(tzinfo=tz)

def solve():
    # Барлық енгізілген мәліметті оқу
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
    
    # Басталу және аяқталу уақыттарын өңдеу
    start_dt = parse_to_utc(lines[0])
    end_dt = parse_to_utc(lines[1])
    
    if start_dt and end_dt:
        # Екі уақыттың айырмасын секундпен есептеу (end - start)
        duration = (end_dt - start_dt).total_seconds()
        # Нәтижені бүтін сан ретінде шығару
        print(int(duration))

if __name__ == "__main__":
    solve()

#17
import math

def solve_radar_coverage():
    try:
        # Input reading
        r = float(input().strip())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
        
        dx = x2 - x1
        dy = y2 - y1
        
        # Quadratic: at^2 + bt + c = 0
        # representing the intersection of segment P(t) = A + t(B-A) and circle x^2 + y^2 = R^2
        a = dx**2 + dy**2
        
        # If the points are the same, check if that point is inside the circle
        if a == 0:
            if x1**2 + y1**2 <= r**2:
                print(f"{0.0:.10f}")
            else:
                print(f"{0.0:.10f}")
            return

        b = 2 * (x1 * dx + y1 * dy)
        c = x1**2 + y1**2 - r**2
        
        discriminant = b**2 - 4 * a * c
        
        if discriminant <= 0:
            # No intersection or tangent (length is 0)
            print(f"{0.0:.10f}")
            return
        
        # Find the two intersection points in terms of t
        sqrt_d = math.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2 * a)
        t2 = (-b + sqrt_d) / (2 * a)
        
        # Clamp the intersection interval [t1, t2] to the segment range [0, 1]
        t_start = max(0, min(t1, t2))
        t_end = min(1, max(t1, t2))
        
        if t_start < t_end:
            # Length = fraction of segment * total segment length
            segment_length = math.sqrt(dx**2 + dy**2)
            inside_length = (t_end - t_start) * segment_length
            print(f"{inside_length:.10f}")
        else:
            print(f"{0.0:.10f}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve_radar_coverage()

#18
import sys

def solve_reflection():
    # Read coordinates for point A
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        x1, y1 = map(float, line1)
        
        # Read coordinates for point B
        line2 = sys.stdin.readline().split()
        if not line2: return
        x2, y2 = map(float, line2)
        
        # Using the formula: x = (x1*y2 + x2*y1) / (y1 + y2)
        # We use absolute values for y to handle points on the same side of the axis
        y1_abs = abs(y1)
        y2_abs = abs(y2)
        
        reflection_x = (x1 * y2_abs + x2 * y1_abs) / (y1_abs + y2_abs)
        reflection_y = 0.0
        
        print(f"{reflection_x:.10f} {reflection_y:.10f}")
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve_reflection()

#19
import math

def solve():
    try:
        r = float(input().strip())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
        
        # Basic distances
        dist_sq = (x2 - x1)**2 + (y2 - y1)**2
        dist_ab = math.sqrt(dist_sq)
        
        # Check if direct path is possible
        # Distance from origin to line AB
        cross_product = abs(x1 * y2 - y1 * x2)
        h = cross_product / dist_ab
        
        # Check if origin projection is within segment AB using dot products
        dot1 = (x2 - x1) * (-x1) + (y2 - y1) * (-y1)
        dot2 = (x1 - x2) * (-x2) + (y1 - y2) * (-y2)
        
        if h >= r or dot1 <= 0 or dot2 <= 0:
            print(f"{dist_ab:.10f}")
        else:
            # Path is blocked by the circle
            oa = math.sqrt(x1**2 + y1**2)
            ob = math.sqrt(x2**2 + y2**2)
            
            # Lengths of tangents
            s1 = math.sqrt(oa**2 - r**2)
            s2 = math.sqrt(ob**2 - r**2)
            
            # Angles
            gamma = math.acos(max(-1, min(1, (x1*x2 + y1*y2) / (oa*ob))))
            alpha = math.acos(r / oa)
            beta = math.acos(r / ob)
            
            theta = gamma - alpha - beta
            arc_len = r * theta
            
            print(f"{(s1 + s2 + arc_len):.10f}")
            
    except (EOFError, ValueError):
        pass

solve()

#20
import sys

def solve_scope_accumulator():
    # Initialize our accumulators
    g = 0  # global variable
    n = 0  # nonlocal variable in outer()
    
    # Read the number of commands
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    num_commands = int(input_data[0])
    pointer = 1
    
    for _ in range(num_commands):
        scope = input_data[pointer]
        value = int(input_data[pointer + 1])
        pointer += 2
        
        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
        # 'local' commands are ignored as they don't affect g or n
            
    print(f"{g} {n}")

if __name__ == "__main__":
    solve_scope_accumulator()

#21
import importlib
import sys

def solve_module_query():
    # Read the number of queries
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    try:
        n = int(input_data[0].strip())
    except ValueError:
        return

    for i in range(1, n + 1):
        try:
            # Split the line into module path and attribute name
            line = input_data[i].split()
            if len(line) < 2:
                continue
            
            module_path, attr_name = line[0], line[1]

            # 1. Attempt to import the module
            try:
                mod = importlib.import_module(module_path)
            except (ImportError, ModuleNotFoundError):
                print("MODULE_NOT_FOUND")
                continue

            # 2. Check for the attribute
            if not hasattr(mod, attr_name):
                print("ATTRIBUTE_NOT_FOUND")
                continue
            
            # 3. Classify as CALLABLE or VALUE
            attr = getattr(mod, attr_name)
            if callable(attr):
                print("CALLABLE")
            else:
                print("VALUE")

        except IndexError:
            break

if __name__ == "__main__":
    solve_module_query()