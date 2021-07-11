# HC1 QR code decoder
### Build by KopyTKG

---

#### Setup
* If you are running linux just run
    *   ```bash
        # File contains pip install -r req.txt
        ./linuxPIP.sh
        ```
* On windows
  * open CMD
  * go to same directory as main.py
  * ```bash
    # Run in cmd
    pip install -r req.txt
    ```

#### USE
* Files
  * input 
    * input goes to src/ directory
      * QR_CODE.png <- contains image of QR code
      * Code.txt <- contains text that is stored in QR code
  * output
    * Decode.txt <- contains decoded information stored in QR code
* Run
  * To run program
    * Make sure at least one of the input files is there
    * ```bash
        # Run python script
        python main.py
        ```