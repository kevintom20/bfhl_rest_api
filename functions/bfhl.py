import json

def handler(event, context):
    try:
        if event['httpMethod'] == 'POST':
            data = json.loads(event['body'])

            user_name = data.get('user_name', '').replace(' ', '_').lower()
            dob = data.get('dob', '')  # In the format ddmmyyyy
            user_id = f"{user_name}_{dob}"

            numbers = [int(i) for i in data.get('data', []) if i.isdigit()]
            alphabets = [i for i in data.get('data', []) if i.isalpha()]

            lower_case_alphabets = [ch for ch in alphabets if ch.islower()]
            highest_lowercase = max(lower_case_alphabets) if lower_case_alphabets else None

            response = {
                "is_success": True,
                "user_id": user_id,
                "email": data.get('email'),
                "roll_number": data.get('roll_number'),
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase": highest_lowercase
            }
            return {
                "statusCode": 200,
                "body": json.dumps(response),
                "headers": {
                    "Content-Type": "application/json"
                }
            }

        elif event['httpMethod'] == 'GET':
            return {
                "statusCode": 200,
                "body": json.dumps({"operation_code": 1}),
                "headers": {
                    "Content-Type": "application/json"
                }
            }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"is_success": False, "error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }
