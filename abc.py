import sys
sys.stderr.write("🔥 Script has started...\n")
sys.stderr.flush()

try:
    import cv2
    sys.stderr.write("✅ cv2 imported\n")
    sys.stderr.flush()
    
    # Test cvzone imports
    try:
        from cvzone.HandTrackingModule import HandDetector
        sys.stderr.write("✅ HandDetector imported\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"❌ Error importing HandDetector: {e}\n")
        sys.stderr.flush()
    
    try:
        from cvzone.ClassificationModule import Classifier
        sys.stderr.write("✅ Classifier imported\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"❌ Error importing Classifier: {e}\n")
        sys.stderr.flush()
    
    import numpy as np
    sys.stderr.write("✅ numpy imported\n")
    sys.stderr.flush()
    
    import math
    sys.stderr.write("✅ math imported\n")
    sys.stderr.flush()
    
    import pyttsx3
    sys.stderr.write("✅ pyttsx3 imported\n")
    sys.stderr.flush()

    print("✅ Environment check passed!", flush=True)
except Exception as e:
    sys.stderr.write(f"❌ Error during import: {e}\n")
    sys.stderr.flush()
    sys.exit(1)
