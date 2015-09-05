//
//  ViewController.swift
//  Calculator
//
//  Created by Mohan, Kishore Kumar on 6/27/14.
//  Copyright (c) 2014 swift. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var firstEntry: NSString?
    var isUserInMiddleOfTypingNumbers:Bool?
    var didUserPressedOperation:Bool?
    var op:String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.clear()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    @IBOutlet var displayLabel: UILabel!
    
    @IBAction func digitPressed(sender: UIButton) {
        self.clear()
        displayLabel.text = sender.currentTitle
    }
   
    
    
    func clear() {
        firstEntry = nil
        isUserInMiddleOfTypingNumbers = nil
        didUserPressedOperation = nil
        displayLabel.text = "0"
    }
   }