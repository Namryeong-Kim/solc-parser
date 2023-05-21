from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time, re, os
from natsort import natsorted


def execute_chrome_driver():
    # ChromeDriver 로그 레벨 설정
    os.environ['webdriver.chrome.loglevel'] = '3'  # 로그 레벨 3은 최소한의 로그 출력을 의미함

    # Chrome WebDriver 경로 설정
    driver_path = './chromedriver'

    chrome_service=Service(driver_path)

    # Chrome WebDriver 인스턴스 생성
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Chrome 창을 표시하지 않고 실행
    driver = webdriver.Chrome(service=chrome_service, options=options)

    return driver

# Solidity 버전 리스트 가져오기
def get_version_list():
    
    driver = execute_chrome_driver()
    url = 'https://github.com/ethereum/solidity/releases'
    driver.get(url)

    versions = []
    current_version = set()
    while True:
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            releases = soup.find_all('a', class_='Link--primary')
            for release in releases:
                version = release.get_text(strip=True).replace('Version ', '')
                version = re.search(r'\d+(\.\d+)*', version).group()
                if version not in current_version:  # 중복 버전인 경우 건너뛰기
                    versions.append(version)
                    current_version.add(version)
                #print(versions)

            next_page_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a.next_page'))
            )
            next_page_attribute = next_page_button.get_attribute('rel')
            if next_page_attribute == 'nofollow':
                break
            else:
                driver.execute_script("arguments[0].click();", next_page_button)
            
        except StaleElementReferenceException:
        # 예외 발생 시 페이지 로딩 대기 후 다시 시도
            time.sleep(1)
            
        except Exception as e:
            #print(f"An error occurred: {str(e)}")
            break
    driver.quit()
    #versions = natsorted(versions)  
    versions = natsorted(versions, key=lambda x: x.split('.')[0])  # 메이저 버전 순으로 정렬
    return versions

def write_version_list(version_list):
    output_file = 'solc_list.txt'
    # 버전 리스트를 파일에 저장
    with open(output_file, 'w') as f:
        for version in version_list:
            f.write(f"{version}\n")

def main():
    version_list = get_version_list()
    write_version_list(version_list)

if __name__ == '__main__':
    main()
