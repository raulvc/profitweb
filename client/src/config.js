const env = 'development'

const refs = {
  development: {
    api: {
      host: 'http://localhost:8000/'
    }
  }
}

export function buildUrl (url) {
  return refs[env].api.host + url
}
