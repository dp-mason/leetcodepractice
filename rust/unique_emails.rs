impl Solution {
    fn parse_email(email:&str) -> Option<String> {
        let mut email_chars = email.chars(); 
        let mut at_char_found = false;
        let mut result = String::new();
        let mut first_plus_active = false;
        // while the iterator does not return None
        while let Some(c) = email_chars.next() {
            match c {
                '@' => {
                    if at_char_found {
                        return None; // invalid email
                    } else {
                        result.push('@');
                        at_char_found = true;
                        first_plus_active = false;
                    }
                },
                '.' if !first_plus_active => {
                    if at_char_found {
                        result.push('.');
                    }
                },
                '+' if !first_plus_active => {
                    if !at_char_found {
                        first_plus_active = true;
                    } else {
                        result.push('+');
                    }
                },
                _ if !first_plus_active => {
                    result.push(c);
                },
                _ => {/* first plus is still active */}
            }
        }
        match result.len() {
            0 => None,
            _ => Some(result)
        }
    }
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        let mut unique_emails:Vec<String> = Vec::new();
        for email in &emails {
            let unique_email = Solution::parse_email(&email);
            match unique_email {
                Some(umail) => {
                    if unique_emails.contains(&umail) == false {
                        println!("unique mail: {umail} found");
                        unique_emails.push(umail);
                    }
                },
                None => {}
            }
            
        }
        unique_emails.len() as i32
    }
}