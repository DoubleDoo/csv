export default function isValidJwt(jwt: string) {
  if (!jwt || jwt.split('.').length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  const exp = new Date(data.exp * 1000);
  const now = new Date();
  // console.log(now)
  // console.log(exp)
  return now < exp;
}