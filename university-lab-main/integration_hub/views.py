import requests
from django.http import JsonResponse

# The Hub function that connects the Spokes
def get_student_report(request, student_id):
    try:
        # 1. Get Data from Student Spoke
        student_res = requests.get(f"http://127.0.0.1:8000/api/students/students/{student_id}/")
        
        # 2. Get Data from Library Spoke
        library_res = requests.get(f"http://127.0.0.1:8000/api/library/records/{student_id}/")
        
        if student_res.status_code == 200:
            student_data = student_res.json()
            # If library record doesn't exist, we'll just say no fines
            library_data = library_res.json() if library_res.status_code == 200 else {"has_fines": False}
            
            # 3. Integrate the data (The Hub Logic)
            report = {
                "id": student_id,
                "name": student_data.get("name"),
                "course": student_data.get("course"),
                "library_status": "Blocked" if library_data.get("has_fines") else "Clear"
            }
            return JsonResponse(report)
        else:
            return JsonResponse({"error": "Student not found"}, status=404)
            
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)