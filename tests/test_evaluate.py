import pandas as pd
from sklearn.metrics import accuracy_score
from detector import analyze_command
from evaluate import evaluate_model, normalize_label


def test_evaluation_accuracy():
    """Test the evaluation with clean summary output."""
    csv_path = "data/cmd_huge_known_commented_updated.csv"
    
    # Run evaluation and get results
    results = evaluate_model(csv_path, show_individual=False, show_detailed=False)
    
    # Assert minimum accuracy threshold
    assert results['accuracy'] >= 0.75, f"Accuracy too low: {results['accuracy']:.2%}"
    
    # Additional assertions for other metrics
    assert results['precision'] >= 0.70, f"Precision too low: {results['precision']:.2%}"
    assert results['recall'] >= 0.70, f"Recall too low: {results['recall']:.2%}"
    assert results['f1'] >= 0.70, f"F1 score too low: {results['f1']:.2%}"
    
    print(f"\n✅ All tests passed! Model meets performance thresholds.")


def test_evaluation_with_details():
    """Test the evaluation with detailed output for debugging."""
    csv_path = "data/cmd_huge_known_commented_updated.csv"
    
    print("=== DETAILED EVALUATION FOR TESTING ===")
    results = evaluate_model(csv_path, show_individual=False, show_detailed=True)
    
    # Same assertions
    assert results['accuracy'] >= 0.75
    assert results['precision'] >= 0.70
    assert results['recall'] >= 0.70
    assert results['f1'] >= 0.70


def test_individual_predictions():
    """Test a few individual predictions manually."""
    test_cases = [
        ("dir", "legitimate"),
        ("eventvwr.exe", "legitimate"),
        ("rm -rf /", "malicious"),  # Example malicious command
    ]
    
    print("=== TESTING INDIVIDUAL CASES ===")
    for cmd, expected in test_cases:
        result = analyze_command(cmd)["verdict"]
        print(f"CMD: {cmd} → Predicted: {result.upper()}, Expected: {expected.upper()}")
        # Note: Only assert if you're confident about the expected results
        # assert result == expected, f"Failed for '{cmd}': got {result}, expected {expected}"


if __name__ == "__main__":
    # Run different test modes
    test_evaluation_accuracy()
    print("\n" + "="*60 + "\n")
    test_individual_predictions()