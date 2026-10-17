from flask import Flask, jsonify
import time

app = Flask(__name__)

# ইউনিক ইউনিকোড সুপারস্ক্রিপ্ট নম্বর জেনারেট করার ফাংশন (যেমন: ⁰⁰⁰¹)
def get_superscript_num(n):
    superscript_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
                       '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
    num_str = f"{n:04d}"  # 4-digit format (0001, 0002...)
    return "".join(superscript_map[digit] for digit in num_str)

# অ্যাকাউন্ট তৈরির ইন্টারনাল লজিক ফাংশন
def create_single_guest_account(index):
    # নিকনেম ও বায়ো সেটআপ
    nickname = f"AYAN-like{get_superscript_num(index)}"
    bio = "TG-@Ayan202\nItz-redeem_cod_ullimited_"
    
    # NOTE: আপনার গেম/সার্ভারের আসল রেজিস্টার API Call এখানে করতে হবে।
    # আপাতত আমরা একটি স্যাম্পল রেসপন্স ফরম্যাট রিটার্ন করছি:
    
    game_id = f"88492{index:04d}"  # ডামি গেম আইডি
    access_token = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.guest_token_{index}" # ডামি টোকেন
    
    return {
        "status": "Successful",
        "access_token": access_token,
        "game_id": game_id,
        "name": nickname,
        "bio": bio
    }

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Guest Account Generator API is Running!"})

@app.route('/generate-guests', methods=['GET', 'POST'])
def generate_guests():
    created_accounts = []
    
    # ২০০ টি অ্যাকাউন্ট তৈরির লুপ
    for i in range(1, 201):
        acc = create_single_guest_account(i)
        created_accounts.append(acc)
        # সময় বা ব্যাকএন্ডের ওপর প্রেশার কমাতে দরকার হলে হালকা ডিলে দেওয়া যায়
        # time.sleep(0.05)
        
    return jsonify({
        "total_created": len(created_accounts),
        "accounts": created_accounts
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
