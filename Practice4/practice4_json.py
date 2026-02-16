import json
import os

# Скрипт орналасқан папканы анықтау
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, "sample-data.json")

print(f"Скрипт папкасы: {script_dir}")
print(f"JSON файлы: {json_file_path}")
print(f"Файл бар ма? {os.path.exists(json_file_path)}")

# Файлдың ішін оқып көрейік
try:
    with open(json_file_path, 'r') as file:
        file_content = file.read()
        print("\nФайлдың алғашқы 200 символы:")
        print(file_content[:200])
        print("-" * 50)
        
        # JSON ретінде талдап көрейік
        data = json.loads(file_content)
        
    # Кестені шығару
    print("\nInterface Status")
    print("=" * 80)
    print(f"{'Description':<50} {'Speed':<10} {'MTU':<10}")
    print(f"{'-'*50:<50} {'-'*10:<10} {'-'*10:<10}")
    
    # Деректерді өңдеу
    if 'imdata' in data:
        for item in data['imdata']:
            if 'l1PhysIf' in item:
                attrs = item['l1PhysIf']['attributes']
                dn = attrs.get('dn', '')
                speed = attrs.get('speed', 'inherit')
                mtu = attrs.get('mtu', '9150')
                print(f"{dn:<50} {speed:<10} {mtu:<10}")
    else:
        print("JSON құрылымы дұрыс емес")
        print("JSON кілттері:", data.keys())
        
except FileNotFoundError:
    print(f"Қате: {json_file_path} файлы табылмады!")
except json.JSONDecodeError as e:
    print(f"JSON форматы қате: {e}")
    print(f"Қате жол: {e.lineno}, қате позиция: {e.colno}")
    print(f"Қате мәтін: {e.msg}")