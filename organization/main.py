#ตัวแปรสำหรับเก็บงานทั้งหมด
tasks = []

#output menu
def show_menu():
    print("\n====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

# เพิ่มงานใหม่ในรายการ
def add_task():
    name = input("📌 ป้อนชื่องาน: ")
    date = input("📅 ป้อนวันที่ (dd/mm/yyyy): ").strip()
    category = input("🌾 ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ").strip()
    tasks.append({'name': name, 'category': category, 'date': date})
    print("✅ เพิ่มงานสำเร็จ")

# แสดงรายการงานทั้งหมด
def show_tasks():
    if not tasks:
        print("❌ยังไม่มีงานในระบบ")
        return
    print("\n📋 รายการงานทั้งหมด:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['date']} - {task['name']} ({task['category']})")

# ลบงานจากรายการ
def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        index = int(input("🔻 ลำดับของงานที่ต้องการลบ: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑 ลบงาน: {removed['name']} แล้ว")
        else:
            print("❌ ไม่พบงานที่ระบุ")
    except ValueError:
        print("⚠️ กรุณากรอกตัวเลข")

# สรุปจำนวนงานในแต่ละประเภท
def summarize_tasks():
    summary = {}
    for task in tasks:
        cat = task['category']
        summary[cat] = summary.get(cat, 0) + 1
    print("\n📊 สรุปจำนวนงานแต่ละประเภท:")
    if not summary:
        print("❌ยังไม่มีงานในระบบ")
    else:
        for cat, count in summary.items():
            print(f"- {cat}: {count} งาน")

#เมนูหลัก
def main():
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks()
        elif choice == '5':
            print("👋 ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        else:
            print("⚠️ กรุณาเลือกหมายเลข 1-5 เท่านั้น")

#เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()
