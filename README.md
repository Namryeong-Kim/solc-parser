# solc-parser

## 기본 형태

```solidity
pragma solidity [version];
```

## 고려해야할 사항

- 최신 버전 사용

<aside>
💡 **경우의 수**

- [x] 0.x
- [x] 0.x.x
- 사용할 수 있는 기호
  - [x] ^ : 최신 마이너 버전
  - [x] ~ : 최신 패치 버전
  - [ ] - : 모든 버전
    * pragma solidity \*
    * pragma solidity \*.0
    * pragma solidity \*.x
    * pragma solidity _._
    * pragma solidity _._.0
    * pragma solidity _._.x
    * pragma solidity _._.\*
    * pragma soldity 0.\*
    * pragma soldity 0._._
    * pragma soldity 0.0.\*
  - [x] = : 특정 버전
  - [x] ≥ : 특정 버전 이상
  - [x] ≤ : 특정 버전 이하
  - [x] > : 특정 버전 초과
  - [x] < : 특정 버전 미만
  - [x] 숫자만 기입
    - pragma solidty 0.x.x
- [x] range 설정
  - ≥0.4.5 ≤0.7.0

</aside>

## 조건에 따른 버전 선택

### 고려해야할 것

<aside>
💡 List

1. 부버전과 일치하는 것 중 가장 높은 버전을 고르면 되는 경우
   - [x] 캐럿 기호(^)
   - [x] ~
   - [x] ≥
   - [x] range
   - [ ] -
2. 추출한 target_version과 동일한 버전을 고르면 되는 경우
   - [x] =
   - [x] ≤
   - [x] 숫자만 기입
3. 입력한 버전의 패치버전에서 -1

   - [x] <

   → 0.8 이런식으로 부버전만 줬을때는 부버전 -1 해줘야 됨

4. 입력한 버전의 패치버전에서 +1
   - [x] >
5. range로 들어온 경우
   - [x] 기호와 버전을 각각 분리해서 저장 → list
   - [x] list[2]의 기호에 따른 1-4 로직 연결

- [x] 기호도 추출할 수 있어야 함
</aside>

## 개선 및 해결해야할 것

<aside>
💡 1. 예외 발생시 페이지 로딩을 1초 기다렸다가 수행함 → output 출력까지 시간이 좀 걸림

→ selenium 너무 무거워서 request 이용하는 형태로 변경

1. 현재는 실행할 때마다 전체 리스트를 크롤링하는 방식 → 따로 파일에 저장해두고 새로운 버전 릴리즈가 나올때 새로운 버전만 추가하는 방식으로 변경해야할 것 같음 - 내림차순으로 정렬해서 for문으로 저장된 파일의 처음과 릴리즈 크롤링한 값이 같다면 새로운 버전이 나온 것이 아니므로 break/return하면 되지 않을까? - [x] 내림차순 정렬 완료 - [x] 파일에 저장하도록 변경
</aside>
