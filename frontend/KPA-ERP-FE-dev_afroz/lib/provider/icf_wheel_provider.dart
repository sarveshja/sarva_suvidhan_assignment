import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
class IcfWheelProvider extends ChangeNotifier {
  bool submitted = false;
  bool isEditing = false;
  bool showSummaryCard = false;
bool showFilterCard = false;  // for filter summary card

  final searchController = TextEditingController();
  final treadDiameterController = TextEditingController(text: "915 (900-1000)");
  final lastShopIssueController = TextEditingController(text: "837 (800-900)");
  final condemningDiaController = TextEditingController(text: "825 (800-900)");
  final wheelGaugeController = TextEditingController(text: "1600 (+2,-1)");

  final List<Map<String, Widget>> allFields = [];
  List<Map<String, Widget>> visibleFields = [];

  String filterFormNumber = '';
  String filterCreatedAt = '';
  String filterCreatedBy = '';

  void initializeFields(List<Map<String, Widget>> fields) {
    allFields.clear();
    allFields.addAll(fields);
    visibleFields = List.from(allFields);
    notifyListeners();
  }

  void filterFields(String query) {
    visibleFields = query.isEmpty
        ? List.from(allFields)
        : allFields
            .where((field) => field.keys.first.toLowerCase().contains(query.toLowerCase()))
            .toList();
    notifyListeners();
  }

 Future<void> applyFilter({String formNumber = '', String createdAt = '', String createdBy = ''}) async {
  filterFormNumber = formNumber;
  filterCreatedAt = createdAt;
  filterCreatedBy = createdBy;

  final uri = Uri.parse('http://localhost:8000/api/icf-wheel/'); // Add query params if needed
  final body = {
    "form_number": formNumber,
    "created_at": createdAt,
    "created_by": createdBy,
  };

  try {
    final response = await http.post(
      uri,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(body),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      // Update your filtered results list with `data`
      showSummaryCard = true;
      notifyListeners();
    } else {
      throw Exception("Filter fetch failed");
    }
  } catch (e) {
    debugPrint("Filter error: $e");
  }
}


void handleSubmit(BuildContext context) async {
  final uri = Uri.parse('http://localhost:8000/api/icf-wheel/'); // Replace with actual API URL

  final body = {
    "tread_diameter": treadDiameterController.text,
    "last_shop_issue": lastShopIssueController.text,
    "condemning_diameter": condemningDiaController.text,
    "wheel_gauge": wheelGaugeController.text,
  };

  try {
    final response = await http.post(
      uri,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(body),
    );

    if (response.statusCode == 200 || response.statusCode == 201) {
      submitted = true;
      isEditing = false;
      notifyListeners();

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Wheel spec form submitted successfully.")),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Submission failed: ${response.statusCode}")),
      );
    }
  } catch (e) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text("Error: ${e.toString()}")),
    );
  }
}


  void handleEdit() {
    isEditing = true;
    notifyListeners();
  }
}
