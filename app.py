from flask import Flask, request, jsonify
from datastructure import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

@app.route('/')
def hello():
    return 'API Server esta Arriba!!'

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Miembro no Encontrado"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.get_json()
    if not member_data or 'first_name' not in member_data or 'age' not in member_data or 'lucky_numbers' not in member_data:
        return jsonify({"error": "Dato invalido"}), 400

    new_member = jackson_family.add_member(member_data)
    return jsonify(new_member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": "Eliminado Exitosamente"}), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)